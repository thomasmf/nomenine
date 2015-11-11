

REGISTER_FLAG( 'detach_threads', 'detach threads' )


ROOT_SCOPE_METHOD( MD( 'Task', 'TASK_FACTORY_single()' ) )


FUNCTION( 'void nom_do_sync( FRAME__TASK task )', """
  task->action->objective( $CA(task) ) ;
  return ;
""" )

FUNCTION( 'void* nom_do_thread_start_routine( void* arg )', """
  nom_do_sync( $C(FRAME__TASK,arg) ) ;
  return NULL ;
""" )

FUNCTION( 'void nom_do_async( FRAME__TASK task )', """
  nom_call_async( nom_do_thread_start_routine, $CAST(void*,task) ) ;
  return ;
""" )

FUNCTION( 'void nom_call_async( void* (*start_routine)( void* arg ), void* arg )', """
  pthread_t* thread = $CAST(pthread_t*,nom_malloc( sizeof( pthread_t ) )) ;

  if ( pthread_create( thread, NULL, start_routine, arg ) ) {
    printf( \"System error. Failed to create thread.\\n\" ) ;
    exit( EX_SOFTWARE ) ;
  }

  $ENABLED( detach_threads,
    pthread_detach( *thread ) ;
  )

  $DISABLED( informative_errors,
    pthread_join( *thread, NULL ) ;
  )

  return ;
""" )

FUNCTION( 'void nom_wait_for_all_activity_to_finish()', """
//  $OUT( finnished. waiting. ) ;
  pthread_exit( NULL ) ;
  return ;
""" )


OBJECT( 'TASK_FACTORY',
  methods = [
    MS( ARG( CW( '@' ), CG( 'ANY', 'context' ), CG( 'ANY', 'action' ), CG( 'ANY', 'that' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, $CA(FRAME__TASK_new( PARAM_context, PARAM_action, PARAM_that )) ) ;
    """ ),
  ]
)


FRAME( 'TASK',
  attributes = [
    A( 'ANY', 'action' ),
    A( 'ANY', 'that' ),
  ],
  methods = [
    MS( ARG( CW( 'schedule' ) ), """
      nom_do_async( ACTION ) ;
      JUMP__return_ANY( CONTEXT, CONTEXT, $NONE ) ;
    """ ),
    MS( ARG( CW( 'action' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->action ) ;
    """ ),
    MS( ARG( CW( 'that' ) ), """
      JUMP__return_ANY( CONTEXT, CONTEXT, ACTION->that ) ;
    """ ),
  ],
  dump = D( '%s', '$DUMP( object->parent )' )
)

